<script>
	import { page } from '$app/stores';
	import { pos, visible } from './store.js';
	import ProfilePopup from './ProfilePopup.svelte';
	import { browser } from '$app/environment';

	let userdata = $page.data.json;
	let popupHeight = 'h-0';

	const handleMouseEvent = (e, type) => {
		if (popupHeight === 'h-0' && type !== 'close') {
			popupHeight = 'h-52';
		} else {
			popupHeight = 'h-0';
		}
	};

	const handleKeyDown = (e, type) => {
		let trueCondition = true;
		if (type === 'key') {
			trueCondition = e.keyCode === 17;
		}

		if (trueCondition) {
			if ($pos !== 'left-0') {
				pos.set('left-0');
				visible.set('opacity-100 z-[10]');
			} else {
				pos.set('left-[-25%]');
				visible.set('opacity-0 z-[-10]');
				handleMouseEvent(e, 'close');
			}
		}
	};
</script>

<div>
	<nav
		class={'flex justify-center h-[100vh] w-[25%] bg-black flex-wrap absolute text-white p-5 pb-16 ' +
			$pos}
	>
		<div class="w-full relative">
			<h1 class="font-mono text-3xl font-extrabold h-10 text-left">SumUp</h1>
			<hr class="bg-white h-0.5 w-full" />

			<button
				class="absolute right-0 top-[-5px] h-8 fill-red-600 w-8"
				on:click={(e) => {
					handleKeyDown(e, 'click');
				}}
			>
				<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" class="pb-2">
					<path
						d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"
					/></svg
				>
			</button>
		</div>
		<div class="w-full h-full flex flex-col items-center justify-end">
			<ProfilePopup height={popupHeight} />
			<button
				class="w-full rounded-lg border-2 border-gray-300 h-16 flex p-2 items-center px-5 hover:bg-gray-700"
				on:click={handleMouseEvent}
			>
				<div class="rounded-3xl border-2 h-10 w-10 border-gray-300 overflow-hidden">
					{#if browser}
						<img src={userdata.profile_photo} alt="..." class="h-full" />
					{/if}
				</div>
				<div class="text-sm ml-5">
					{#if browser}
						{userdata.username} <br /> {userdata.email}
					{:else}
						... <br /> ...
					{/if}
				</div>
			</button>
		</div>
	</nav>

	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div
		class={'absolute h-[100vh] w-[75%] bg-black bg-opacity-30 left-[25%] ' + $visible}
		on:click={(e) => {
			handleKeyDown(e, 'click');
		}}
	></div>

	<slot />
</div>

<svelte:window
	on:keydown={(e) => {
		handleKeyDown(e, 'key');
	}}
/>
